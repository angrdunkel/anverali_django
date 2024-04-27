class BaseMixin():
    def is_ajax(self):
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return True
        return False
    
    def get_template_names(self):
        if self.is_ajax():
            return [self.template_name_ajax]
        return [self.template_name]