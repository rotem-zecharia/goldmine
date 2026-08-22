# mherrmann/helium

Lighter web automation with Python

## installation

To get started with Helium, you need Python 3 and Chrome or Firefox.

I would recommend creating a virtual environment. This lets you install Helium
for just your current project, instead of globally on your whole computer.

To create and activate a virtual environment, type the following commands into
a command prompt window:

```bash
python3 -m venv venv

## tools

driver.execute_script("alert('Hi!');")
```

So in other words, you don't lose anything by using Helium over pure Selenium.

In addition to its more high-level API, Helium simplifies further tasks that are
traditionally painful in Selenium:

- **iFrames:** Unlike Selenium, Helium lets you interact with elements inside
  nested iFrames, without having to first "switch to" the iFrame.
- **Window management.** Helium notices when popups open or close and focuses /
  defocuses them like a user would. You can also easily switch to a window by
  (parts of) its title. No more having to iterate over Selenium window handles.
- **Implicit waits.** By default, if you try click on an element with Selenium
  and that element is not yet present on the page, your script fails. Helium by
  default waits up to 10 seconds for the element to appear.
- **Explicit waits.** Helium gives you a much nicer API for waiting for a
  condition on the web page to become true. For example: To wait for an element
  to appear in Selenium, you would write:
  ```python
  element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "myDynamicElement"))
  )
  ```
  With Helium, you can write:
  ```python
  wait_until(Button('Download').exists)
  ```
