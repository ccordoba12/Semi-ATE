import os
from ATE.spyder.widgets.coding.generators import test_proper_generator


class test_target_generator(test_proper_generator):
    """Generator for the Test Class."""

    def __init__(self, project_path, definition, do_update=False):
        super().__init__(project_path, definition, do_update=do_update)

    def _generate_relative_path(self):
        hardware = self.definition['hardware']
        base = self.definition['base']
        base_class = self.definition['base_class']

        return os.path.join('src', hardware, base, base_class)
