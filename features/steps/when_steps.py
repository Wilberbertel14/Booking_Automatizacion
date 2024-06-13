from behave import when

@when('I click on the "{menu_option}" "{element_type}"')
def click_menu_option(context, menu_option, element_type):
    context.home_page.click_menu_option(menu_option)