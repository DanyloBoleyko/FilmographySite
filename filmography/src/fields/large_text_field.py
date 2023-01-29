from django.db.models import TextField


class LargeTextField(TextField):
    """A TextField that does not strip whitespace at the beginning/end of
        its value.  Might be important for markup/code."""

    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(LargeTextField, self).formfield(**kwargs)
