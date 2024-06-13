from behave import then

@then('I should be in the "home" page')
def should_be_in_home_page(context):
    assert context.home_page.is_home_page()

@then('The URL of the page should match the expected "{URL}"')
def url_should_match(context, URL):
    assert context.browser.current_url == URL