from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False,slow_mo=500) # headless=False : ให้หน้า browser ขึ้นมาเวลารันเป็นเวลา slow_mo=500 : pop-up ขึ้นมาเป็นเวลา 0.5 secs
    # Create a new page
    page = browser.new_page()

    target_url = 'https://bootswatch.com/default'
    # Visit any website 
    page.goto(target_url)

    ################ Role Locator #################

    # E.g. Locate a button element with "Default button" text
    page.get_by_role('button',name="Default button").highlight()

    # E.g. Locate a heading element 
    page.get_by_role('heading',name='Heading 2').highlight()

    # Others radio , checkbox 

    ################ Input Field Locator #################

    # Allows locating input elements by the text of the associated <label> or aria-labelledby element, or by the aria-label attribute.
    page.get_by_label('Email address').highlight() # ไปที่ tag label 'Email address' (exact match) แล้ว highlight tag input ในลำดับชั้นเดียวกับ label ที่เจอ

    # Allows locating input elements by the placeholder text.
    page.get_by_placeholder('Enter email').highlight()

    ################ Inner Text Locator #################

    # Allows locating elements that contain given text.
    page.get_by_text('Basic',exact=False).highlight() # highlight ก้อน text นั้น เมื่อ contains 'Basic'
    page.get_by_text('Basic',exact=True).highlight() # highlight ก้อน text นั้น เมื่อ = 'Basic'

    ################ Alt Text Locator #################

    # Allows locating elements by their alt text.
    page.get_by_alt_text('ads via Carbon').highlight()

    ################ Title Locator #################

    # Allows locating elements by their title attribute.
    page.get_by_title('attribute').highlight()

    ################ CSS Selector #################

    # Allows locating elements by their title attribute.
    page.locator('h1').highlight() # all tag h1
    page.locator('button.btn btn-success').highlight() # all tag button & class 'btn btn-success'
    page.locator('button#btnGroupDrop2').click() # all tag button & id 'btnGroupDrop2'
    page.locator('input[readonly]').highlight() # all tag input & attribute 'readonly'
    page.locator("input[value='correct value']").highlight() # all tag input & attribute 'value'='correct value'
    page.locator('nav.bg-dark a.nav-link.active').highlight() # all tag nav & class 'bg-dark' -> tag a & class 'nav-link' & class 'active'

    # e.g. pseudo classes 
    page.locator("h1:text('Nav')").highlight() # all tag h1 & contains 'Nav' text (highlight ทั้งก้อน)
    page.locator("h1:text-is('Nav')").highlight() # all tag h1 & = 'Nav' text (highlight ทั้งก้อน)
    page.locator("div.dropdown-menu").highlight() # เลือกทั้งหมด 
    page.locator("div.dropdown-menu:visible").highlight() # เลือกเฉพาะที่เราเห็น visible
    page.locator(":nth-match(button.btn-primary,5)").highlight() # เฉพาะ tag button & class 'btn-primary' [5 of ....] 
    page.locator(":nth-match(button:text('Primary'),1)").highlight() # เฉพาะ tag button & class 'btn-primary' อันดับที่ 1 

    ################ XPath Locator #################
    page.locator("//h1").highlight() # all tag h1
    page.locator("//h1[@id='navbars']").highlight() # all tag h1 & attribute ชื่อ id มีค่า = 'navbars' (exact match)
    page.locator("//input[@readonly]").highlight() # all tag input & attribute ชื่อ readonly 

    ################# XPath Functions #################
    page.locator("//h1[text()='Heading 1']").highlight() # all tag h1 & text 'Heading 1' (exact match)
    page.locator("//h1[contains(text(),'Head')]").highlight() # all tag h1 & text 'Head' (contains)
    page.locator("//input[contains(@value,'correct')]").highlight() # all tag input & attribute ที่ชื่อ value มีค่า 'correct' (contains)

    ################# Other Locators #################
    page.get_by_role('button',name='Primary').locator("nth=0").highlight()
    page.locator('button').locator("nth=18").highlight()
    page.get_by_label('Email address').locator('..').highlight() # ไปที่ tag label 'Email address' และ highlight parent tag ของมัน 
    page.locator('div.dropdown-menu').locator('visible=True').highlight()
    page.get_by_role('heading').filter(has_text='Heading').highlight() # all tag ที่ทำหน้าที่เป็น heading โดย filter เลือกเฉพาะอันที่ text 'Heading' เท่านั้น (contains)
    page.locator('fieldset div').filter(has=page.get_by_label('Password')).highlight() # all tag 'fieldset' -> tag 'div' โดย filter เลือกเฉพาะอันที่ tag 'div' ที่ข้างในมี tag 'label' ที่ text 'Password' (exact match)

    ################# Mouse Actions #################
    button = page.get_by_role('button',name='Block Button').first # เอาอันแรกสุด
    button.click() # click ซ้าย
    button.dblclick(delay=500) # double click โดยเว้นช่วง 0.5 secs
    button.click(button='right') # click ขวา
    button.click(modifiers=['Shift','Alt']) # click ซ้าย + ปุ่ม shift + ปุ่ม Alt
    button.hover()

    ################# Input Field Actions #################
    input = page.get_by_placeholder('Enter email')
    input.fill('Boat_:)@gmail.com') # fill ข้อมูลลงไปใน location ของตัวแปร input
    input.clear('Boat_:)@gmail.com') # clear input box
    input.type('Boat_:)@gmail.com',delay=200) # type ข้อมูลลงไปใน location ของตัวแปร input โดยตอน type จะเว้นช่วงเวลาแต่ละตัวอักษร 0.2 secs
    input.input_value() # return current filled value in input box  

    ################# Checkbox and Radio Inputs #################
    radio_option2 = page.get_by_label('Option two can be something else and selecting it will deselect option one')
    radio_option2.check()

    checkbox = page.get_by_label('Default checkbox')
    checkbox.check()
    checkbox.set_checked(True)
    
    checkbox.uncheck()
    checkbox.set_checked(False)

    checkbox.is_checked()

    checkbox.click()

    # switch = page.get_by_label('Default switch checkbox input')
    # switch.check()
    # switch.set_checked(True)
    
    # switch.uncheck()
    # switch.set_checked(False)

    # switch.is_checked()

    # switch.click()

    ################# Option/Select Menu #################
    select = page.get_by_label('Example select')
    select.select_option('4')

    multi_select = page.get_by_label('Example multiple select')
    multi_select.select_option(['2','4'])

    ################# Dropdown Menu #################
    # e.g. click dropdown link อันสุดท้ายจากปัจจุบัน 
    page.locator('button#btnGroupDrop1').click()
    page.locator("div.dropdown-menu:visible a:text('Dropdown link')").last.click()

    ################# Upload Files #################
   


    browser.close() # ปิด browser เมื่อ task ทั้งหมดเสร็จแล้ว 