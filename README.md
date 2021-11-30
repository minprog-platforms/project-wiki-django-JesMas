
# Encyclopedia design document

A design document describing the mechanisms of a wiki containing various entries which can be edited or browsed. New entries can also be added. The final look of the website is also shown here in ui sketches.


## HTML Pages in website

* **Index page**: shows links to all names of entries in the encyclopedia) 
* **Entry page**: ascessed by wiki/TITLE shows page for specific entry. If TITLE is not an entry redirect to title error page. Has button for edit page redirects to edit entry page.
* **Edit entry page**: give a page to edit the existing markdown in entry with save button that
* **Title error page**: shows error to say entry does not exist with buttom to go to index page
* **new entry page**: Has a textbox for title of entry and a textarea for markdown content of entry. Has save buttom that saves entry, checks if entry title already exits and if it does take to entry error page, if not save entry and go to entry page
* **entry error page**: shows error when entry already exits, has button to go back to new entry page

## Layout elements

These elements are present in every page (except error pages) in the navigation bars.

* Search(textfield): searchbox in sidebar to search entries, if name matches entry then take to that entry page else show results page with entries that match the substring. The results page should also link to all entries shown.
* New page(button): buttom in sidebar to create a new entry, takes to new entry page.
* Random page (button): Takes you to a random entry page.
* Create (button): Takes you to the create entry page.
* Edit (button): Takes you to the edit entry page.
## Page design images

![homepage](images/homepage_wiki.jpg?raw=true "homepage")
![search page](images/Search_page.jpg?raw=true "search page")
![create entry](images/Create_entry.jpg?raw=true "create entry")
![edit entry](images/Edit_entry.jpg?raw=true "edit entry")
![entry page](images/Entry_page.jpg?raw=true "entry page")
![error page](images/Error_page.jpg?raw=true "error page")

