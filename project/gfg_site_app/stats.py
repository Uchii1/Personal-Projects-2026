# stats.py created to 
from django.db.models import Avg, Count, Q
from .models import QuizAttempt, AnswerRecord
from collections import defaultdict

# Percentages to be in nearest whole number for simplicicity
def _pct(correct, total):
    return int(correct/total * 100) if total else 0

# Summary of user attemps displayed on top of the My Progress page
def summary(user):
    from django.db.models import Sum
    agg = QuizAttempt.objects.filter(user=user).aggregate(
        attempts=Count("id"), score=Sum("score"), total=Sum("total"))
    return {"attempts": agg["attempts"],
            "overall_percent": _pct(agg["score"] or 0, agg["total"] or 0)}


# CHART 1: Overall score over time
def score_over_time(user):
    # Processing % score per attempt, oldest first.
    attempts = QuizAttempt.objects.filter(user=user).select_related("gfg").order_by("timestamp")
    return [
        # Showing date timestamp on x-axis
        {"date": a.timestamp.strftime("%d %b"), "quiz": a.gfg.gfg_name, "percent": a.percent}
        for a in attempts
    ]

# CHART 2: Strengths and weak spots graph
# Filters results of accuracy by tag 

# Removes tags for which the user has attempted less than 3 questions
def accuracy_by_tag(user, min_answers=3, limit=None):

    # Fetched snwer records of the user and tag list for related questions
    rows = (AnswerRecord.objects
            .filter(attempt__user=user, question__isnull=False)
            .values_list("question__tags", "is_correct"))
    counts = defaultdict(lambda: [0, 0])              # counts[tag] = [correct, total]
    
    # Normalise tags: strip whitespace, lowercase, skip non-strings
    for tags, ok in rows:
        clean = {t.strip().lower() for t in (tags or []) if isinstance(t, str) and t.strip()}
        for tag in clean:
            counts[tag][0] += int(ok)
            counts[tag][1] += 1
     # Build output list, excluding tags below the minimum answer threshold
    out = [{"tag": t.title(), "percent": _pct(c, n), "answered": n}
           for t, (c, n) in counts.items() if n >= min_answers]    
    out = sorted(out, key=lambda x: x["percent"])
     # Apply optional limit (currently set to 8)
    return out[:limit] if limit else out



# CHART 3: Performance per main topic bar chart
def accuracy_by_type(user):
    # Only shows topics for whihc the user has attempted a question 
    rows = (AnswerRecord.objects
            .filter(attempt__user=user, question__isnull=False)
            .values_list("question__gfg__gfg_name", "is_correct"))
    counts = defaultdict(lambda: [0, 0])          # type -> [correct, total], with 0 as defaults
    for name, ok in rows:
        base = name.replace(" - Advanced", "").strip()
        counts[base][0] += int(ok)
        counts[base][1] += 1
    return [{"type": t, "percent": _pct(c, n), "answered": n}
            for t, (c, n) in sorted(counts.items())]