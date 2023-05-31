
from playwright.sync_api import expect

def test_dynamicid(page):
    page.goto("/dynamicid")
    page.click("text=Button with Dynamic ID")


def test_Class_attribute(page):
    page.goto("/classattr")
    page.click(".btn-primary")
    page.on("dialog", lambda dialog: dialog.dismiss())
    

def test_hidden_button(page):
    page.goto("/hiddenlayers")
    page.click(".btn-success")
    expect(page.locator(".btn-primary")).to_be_visible()



def test_load_delay(page):
    page.goto("/")
    page.click("text=Load Delay")
    expect(page.locator(".btn-primary")).to_be_visible()
    page.click(".btn-primary")



def test_AJAX(page):
    page.goto("/ajax")
    page.click("#ajaxButton")
    page.click("text=Data loaded with AJAX get request.")



def test_client_side_delay(page):
    page.goto("/clientdelay")
    page.click("#ajaxButton")
    page.click("text=Data calculated on the client side.")



def test_click(page):
    page.goto("/")
    page.click("text=Click")
    page.click("#badButton")
    page.click("#badButton")
    expect(page.locator("#badButton")).to_have_class("btn btn-success")



def test_text_input(page):
    page.goto("/textinput")
    page.fill("#newButtonName", "Top kek")
    page.click("#updatingButton")
    expect(page.locator("#updatingButton")).to_have_text("Top kek")


def test_scrollbars(page):
    page.goto("/scrollbars")
    page.click("#hidingButton")
   


def test_verifytext(page):
    page.goto("/verifytext")
    expect(page.locator(".bg-primary")).to_have_text("Welcome UserName!")



''' def test_progressbar(page):
    page.goto("/progressbar")
    page.click("#startButton")
    page.inner_text("#progressBar[aria-valuenow='75']")
    page.click("#stopButton")
    expect(page.locator("#result")).to_contain_text("0") '''



def test_visibility(page):
    page.goto("/visibility")
    page.click("#hideButton")
    expect(page.locator("#hideButton")).to_be_visible() and page.locator("button").to_be_hidden()


def test_sampleapp_login_logout(page):
    page.goto("/sampleapp")
    page.get_by_placeholder("User Name").fill("gg")
    page.locator("[name=\"Password\"]").fill("pwd")
    page.click("#login")
    expect(page.locator("#loginstatus")).to_have_text("Welcome, gg!")
#logout
    page.click("#login")
    expect(page.locator("#loginstatus")).to_have_text("User logged out.")


def test_sampleapp_no_password(page):
    page.goto("/sampleapp")
    page.get_by_placeholder("User Name").fill("gg")
    page.click("#login")
    expect(page.locator("#loginstatus")).to_have_text("Invalid username/password")


def test_sampleapp_no_user(page):
    page.goto("/sampleapp")
    page.locator("[name=\"Password\"]").fill("pwd")
    page.click("#login")
    expect(page.locator("#loginstatus")).to_have_text("Invalid username/password")


def test_sampleapp_no_data(page):
    page.goto("/sampleapp")
    page.click("#login")
    expect(page.locator("#loginstatus")).to_have_text("Invalid username/password")


def test_mouseover(page):
    page.goto("/mouseover")
    page.click("text=Click me")
    page.click("text=Click me")
    expect(page.locator("#clickCount")).to_contain_text("2")


def test_space(page):
    page.goto("/nbsp")
    page.click("text=My Button")



def test_overlapped_field(page):
    page.goto("/overlapped")
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("Top kek")
  


