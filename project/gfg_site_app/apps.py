from django.apps import AppConfig



class GfgSiteAppConfig(AppConfig):
    name = "gfg_site_app"

    def ready(self):
        from django.contrib.auth.signals import user_logged_in

        def flag_cookie(sender, request, user, **kwargs):
            request.session["show_cookie"] = True

        user_logged_in.connect(flag_cookie)

