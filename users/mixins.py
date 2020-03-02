from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin


class LoggedOutOnlyView(UserPassesTestMixin):

    permission_denied_message = "page not found"

    def test_func(self):  # this def
        return not self.request.user.is_authenticated

    def handle_no_permission(self):

        return redirect("core:home")
