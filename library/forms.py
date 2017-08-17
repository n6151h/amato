from django import forms

class AmatoModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        """
        This method is used to convert objects into strings; it's used to
        generate the labels for the choices presented by this object. Subclasses
        can override this method to customize the display of the choices.
        """
        # Then return what you'd like to display
        return "{}".format(obj.title)