from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from decouple import config
import time

def submit_application():
    try:
        checkbox = driver.find_element(By.CSS_SELECTOR, 'footer div.relative.mt5.ph5')
        checkbox.click()
        time.sleep(2)
    except NoSuchElementException:
        pass

    available_button.click()

    time.sleep(2)


def discard_application():
    try:
        dismiss_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
        dismiss_button.click()
    except NoSuchElementException:
        pass

    time.sleep(2)

    try:
        footer_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__confirm-dialog-btn.artdeco-button--primary')
        if footer_button.get_attribute('data-control-name') == 'discard_application_confirm_btn':
            footer_button.click()
    except NoSuchElementException:
        pass

    time.sleep(2)

    print('The application was too complex, skipping')

def check_for_modal():
    pass


s = Service("C:\Development\chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get\
    ("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101165590&keywords=graduate%20software%20engineer&location=United%20Kingdom")

driver.maximize_window()
login_tag = driver.find_element(By.CSS_SELECTOR, 'div.nav__cta-container a.nav__button-secondary')
login_tag.click()


email_tag = driver.find_element(By.ID, 'username')
email_tag.send_keys(config('EMAIL'))
password_tag = driver.find_element(By.ID, 'password')
password_tag.send_keys(config('PASSWORD'))
password_tag.send_keys(Keys.ENTER)

time.sleep(2)

last_page_tag = driver.find_elements(By.CLASS_NAME, 'artdeco-pagination__indicator--number')[-1]
no_of_pages = int(last_page_tag.get_attribute('data-test-pagination-page-btn'))

url = driver.current_url

for page in range(no_of_pages+1):
    if page == 0:
        continue
    elif page > 1:
        new_url = url + f'&start={page*25 - 25}'
        driver.get(new_url)
        time.sleep(2)
    job_links = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item.occludable-update.p0.relative.ember-view')
    for job in job_links:
        job.click()

        time.sleep(2)

        try:
            apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
            apply_button.click()
        except NoSuchElementException:
            print('You have already applied to this job')
            continue

        time.sleep(2)

        available_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
        if available_button.get_attribute('aria-label') == 'Submit application':
            submit_application()
            try:
                dismiss = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
                dismiss.click()
            except NoSuchElementException:
                pass
            finally:
                try:
                    dismiss_toast = driver.find_element(By.CSS_SELECTOR, 'li.artdeco-toast-item '
                                                                         'button.artdeco-toast-item__dismiss')
                    dismiss_toast.click()
                    time.sleep(2)
                except NoSuchElementException:
                    continue
        elif available_button.get_attribute('aria-label') == 'Continue to next step':
            available_button.click()
            time.sleep(2)
            review_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
            if review_button.get_attribute('aria-label') == 'Review your application':
                review_button.click()
                time.sleep(2)
                available_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
                if available_button.get_attribute('aria-label') == 'Submit application':
                    submit_application()
                    try:
                        dismiss = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
                        dismiss.click()
                        time.sleep(2)
                    except NoSuchElementException:
                        pass
                    finally:
                        try:
                            dismiss_toast2 = driver.find_element(By.CSS_SELECTOR, 'li.artdeco-toast-item '
                                                                                 'button.artdeco-toast-item__dismiss')
                            dismiss_toast2.click()
                            time.sleep(2)
                        except NoSuchElementException:
                            continue
                else:
                    discard_application()
                    continue
            else:
                discard_application()
                continue

        else:
            discard_application()
            continue



    # hover = ActionChains(driver).move_to_element(job)
    # hover.perform()
    # title = job.find_element(By.CLASS_NAME, 'job-card-list__entity-lockup.artdeco-entity-lockup.artdeco-entity-lockup--size-4.ember-view')
    # title.click()
    # time.sleep(2)
    #
    # try:
    #     apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
    #     apply_button.send_keys(Keys.ENTER)
    # except NoSuchElementException:
    #     continue
    #
    #
    # time.sleep(3)
    #
    # try:
    #     follow_checkbox = driver.find_element(By.XPATH, '//*[@id="ember403"]/div/form/footer/div[1]')
    #     follow_checkbox.click()
    # except NoSuchElementException:
    #     pass
    #
    # time.sleep(2)
    # try:
    #     submit_button = driver.find_element(By.XPATH, '//*[@id="ember1314"]')
    #     submit_button.send_keys(Keys.ENTER)
    # except NoSuchElementException:
    #     try:
    #         close_button = driver.find_element(By.XPATH, '//*[@id="ember1576"]')
    #         close_button.click()
    #     except NoSuchElementException:
    #         pass