from django.conf import settings
from pprint import pprint
import os
from importlib import import_module, util


# Core TemplateHelper class
class TemplateHelper:

    # ? Map context variables to template class/value/variables names
    def map_context(context):

        #! Menu Fixed (vertical support only)
        if context.get("layout") == "vertical":
            if context.get("menu_fixed") is True:
                context["menu_fixed_class"] = "layout-menu-fixed"
            else:
                context["menu_fixed_class"] = ""

        # Content Layout
        if context.get("content_layout") == "wide":
            context["container_class"] = "container-fluid"
            context["content_layout_class"] = "layout-wide"
        else:
            context["container_class"] = "container-xxl"
            context["content_layout_class"] = "layout-compact"


    # Get theme variables by scope
    def get_theme_variables(scope):
        return settings.THEME_VARIABLES[scope]

    # Set the current page layout and init the layout bootstrap file
    def set_layout(view, context={}):
        # Extract layout from the view path
        layout = os.path.splitext(view)[0].split("/")[0]

        # Get module path
        module = f"templates.{settings.THEME_LAYOUT_DIR.replace('/', '.')}.bootstrap.{layout}"

        # Check if the bootstrap file is exist
        if util.find_spec(module) is not None:
            # Auto import and init the default bootstrap.py file from the theme
            TemplateBootstrap = TemplateHelper.import_class(
                module, f"TemplateBootstrap{layout.title().replace('_', '')}"
            )
            TemplateBootstrap.init(context)
        else:
            module = f"templates.{settings.THEME_LAYOUT_DIR.replace('/', '.')}.bootstrap.default"

            TemplateBootstrap = TemplateHelper.import_class(
                module, "TemplateBootstrapDefault"
            )
            TemplateBootstrap.init(context)

        return f"{settings.THEME_LAYOUT_DIR}/{view}"

    # Import a module by string
    def import_class(fromModule, import_className):
        pprint(f"Loading {import_className} from {fromModule}")
        module = import_module(fromModule)
        return getattr(module, import_className)
