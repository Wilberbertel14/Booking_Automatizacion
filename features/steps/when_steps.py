from behave import when

@when('the user clicks on the register button')
def step_impl(context):
    context.home_page.click_alojamiento_button()
    context.home_page.click_vuelo_button()
    context.home_page.click_alquiler_button()
    context.home_page.click_atraccion_button()
    context.home_page.click_taxis_button()

    

