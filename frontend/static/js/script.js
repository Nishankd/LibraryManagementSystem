// Function to get the value of a cookie by name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie contains the name we're looking for
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                // Extract and return the cookie value
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function createBook() {
    var title = document.getElementById('title').value;
    var author = document.getElementById('author').value;

    var shared_with_info = document.getElementById('shared_with').value
    var shared_permission_info = document.getElementById('shared_permissions').value;

    // Get CSRF token
    var csrftoken = getCookie('csrftoken');

    // Send AJAX request with CSRF token and updated payload
    fetch('/api/book/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            title: document.getElementById('title').value,
            author: document.getElementById('author').value,
            shared_with: [shared_with_info],
            shared_permissions: [shared_permission_info]
        })

    })
    .then(response => response.json())
    .then(response => {
        // page lai reload garni after successful creation
        getBookList();
        // Clear input fields create vaisakesi
        document.getElementById('title').value = '';
        document.getElementById('author').value = '';
        document.getElementById('shared_with').value = '';
        document.getElementById('permission').value = '';
    })
    .catch(error => {
        console.error('Error creating book:', error);
    });
}


// Fetch data from the rest API endpoint
function getBookList() {
    fetch('/api/book/')
    .then(response => response.json())
    .then(books => {
        console.log('Books:', books);
        displayBooks(books);
    })
    .catch(error => {
        // Handle error
        console.error('Error Fetching Data', error);
    });
}

// Function to display books on the page
function displayBooks(books) {
    var bookList = document.getElementById('list-book');

    // Clear existing content
    bookList.innerHTML = '';

    // Loop through each book and append it to the list
    books.forEach(function (book) {
        var listItem = document.createElement('li');
        listItem.className = 'book-item';
        var permissions = book.permission_given.join(" ");
        var permissionText = !!permissions ? permissions : "No permission Given";
        var sharedWithNames = book.shared_with_names.join(", ");

        // Customize the HTML structures based on your data model
        listItem.innerHTML =
            '<strong>Title:</strong> ' + book.title + '<br>' +
            '<strong>Author:</strong> ' + book.author + '<br>' +
            '<strong>Created by:</strong> ' + book.created_by.username + '<br>' +
            '<strong>Shared With:</strong> ' + sharedWithNames + '<br>' +
            '<strong>Shared Permissions:</strong> ' + permissionText + '<br>' +
            '<div class="book-details">' +
            '<a href="/detail/' + book.id + '" class="btn-view-details">View Details</a>' +
            '</div>';



        bookList.appendChild(listItem);
    });
}

// Initial call to get the book list when the page loads
getBookList();
