BTN_NEW_TEST_CENTER = "//a[text() = 'New Test Center']"
BTN_SEARCH = "//button[text() = 'Search']"
DROPDOWN_NAME = "label[for='englishName'] + div select"
FILTER_FIELD_NAME = '#englishName'
DROPDOWN_CITY = "label[for='city'] + div select"
DROPDOWN_STATUSES = '#status'

ICON_DOTS = 'tr:nth-child(1) td[data-label="Actions"]'
ICON_VIEW_ACTION = 'tr:nth-child(1) td[data-label="Actions"] li:nth-child(1) a'
ICON_EDIT_ACTION = 'tr:nth-child(1) td[data-label="Actions"] li:nth-child(2) a'
ICON_REMOVE_ACTION = 'tr:nth-child(1) td[data-label="Actions"] li:nth-child(3) a'

BTN_CREATE_TEST_CENTER = "//button[text() = 'Create Test Center']"
BTN_CANCEL = "//button[text() = 'Cancel']"
FIELD_NAME = '#name'
DROPDOWN_COUNTRY = '#country'
DROPDOWN_CATEGORY = '.arrow'
DROPDOWN_CATEGORY_ITEM = '.multiselect__element span span'
FIELD_CITY = '#city'
FIELD_ADDRESS = '#address'
FIELD_CONTACT_PHONE = '#phoneNumber'
DROPDOWN_LEGISLATOR = '//*[@class="multiselect__select"]'
DEFAULT_LEGISLATOR = '//*[@class="multiselect__option multiselect__option--highlight"]'
ALL_LEGISLATORS = '//*[@class="multiselect__option"]'
FIELD_TEST_CENTER_OWNER_NAME = '#testCenterOwnerName'
FIELD_TEST_CENTER_OWNER_EMAIL = '#testCenterOwnerEmail'

TITLE = 'h1'
locator = "//span[@class='details-list__title' and text()='{}']/following-sibling::div/span"
NAME = locator.format('Name')
ADDRESS = locator.format('Address')
SUPPORTED_CATEGORIES = locator.format('Supported categories')
COUNTRY = locator.format('Country')
CITY = locator.format('City')
STATUS = locator.format('Status')
PHONE_NUMBER = locator.format('Phone Number')
LEGISLATOR = locator.format('Legislator')
TEST_CENTER_OWNER_NAME = locator.format('Test Center Owner Name')
TEST_CENTER_OWNER_EMAIL = locator.format('Test Center Owner Email')
WARNING_TEST_CENTER_OWNER_EMAIL = 'div.validation-message.validation-message--default > span > span'

EDIT_TCENTER = '//*[@id="app"]//h1'
FIELD_EDIT_NAME = '//*[@id="name"]'
FIELD_EDIT_CITY = '//*[@id="city"]'
FIELD_EDIT_ADDRESS = '//*[@id="address"]'
FIELD_EDIT_POSTAL_CODE = '//*[@id="postalCode"]'
FIELD_EDIT_PHONE_NUMBER = '//*[@id="phoneNumber"]'
FIELD_EDIT_OWNER_NAME = '//*[@id="testCenterOwnerName"]'
SELECT_EDIT_LEGISLATOR = '//*[@class="multiselect__select"]'
SELECTED_EDIT_LEGISLATOR = '//*[text() = "Legislator"]/..//*[@class="multiselect__option"]'
SELECT_EDIT_CATEGORY = '//*[@class="input-group__wrapper"]'
FIELD_EDIT_OWNER_EMAIL = '//*[@id="testCenterOwnerEmail"]'
BTN_EDIT_TCENTER = '//button[text() = "Edit Test Center"]'
TCENTER_SUCCESSFULLY_UPDATED = '//*[@class="alert-message alert-message--success"]'
EMAI_ALREADY_USE = '//*[@id="testCenterOwnerEmail"]/../..' \
                   '//*[@class="validation-message__text validation-message__text--error"]'