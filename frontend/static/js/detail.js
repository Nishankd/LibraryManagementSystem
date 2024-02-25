//function setBookId(id) {
//    bookId = id;
//}
//
//function updateBook(bookId) {
//    var title = document.getElementById('edit-title').value;
//    var author = document.getElementById('edit-author').value;
//    var shared_with_info = document.getElementById('shared_with').value
//    var shared_permission_info = document.getElementById('shared_permissions').value;
//
//    // Get CSRF token
//    var csrftoken = getCookie('csrftoken');
//
//    // Send AJAX PUT request with updated data and CSRF token
//    fetch('/api/book/' + bookId + '/', {
//        method: 'PUT',
//        headers: {
//            'Content-Type': 'application/json',
//            'X-CSRFToken': csrftoken
//        },
//        body: JSON.stringify({
//            title: title,
//            author: author,
//            shared_with: [shared_with_info],
//            shared_permissions: [shared_permission_info]
//        })
//    })
//    .then(response => {
//        if (response.ok) {
//            getBookDetails(bookId);
//
//            // Hide edit form and show book details
//            document.getElementById('edit-book-form').classList.add('hidden');
////            document.getElementById('book-details').classList.remove('hidden');
//
//        } else {
//            console.error('Error updating book:', response.statusText);
//        }
//    })
//    .catch(error => {
//        console.error('Error sending update request:', error);
//    });
//}
//
//
//// Function to fetch book details from the API
//function getBookDetails(bookId) {
//    fetch('/api/book/' + bookId + '/')
//        .then(response => {
//            if (!response.ok) {
//                throw new Error('Network response was not ok');
//            }
//            return response.json();
//        })
//        .then(book => {
//            // Log the retrieved book data to the console
//            console.log('Book details:', book);
//
//            // Update UI elements with book data
//            document.getElementById('title').textContent = book.title;
//            document.getElementById('author').textContent = book.author;
//            document.getElementById('created_by').textContent = book.created_by.username;
//            document.getElementById('shared_with_names').textContent = book.shared_with_names;
//            document.getElementById('permission_given').textContent = book.permission_given;
//        })  // Missing closing parenthesis here
//        .catch(error => {
//            console.error('Error fetching book details:', error);
//        });
//}
//
//// Function to handle delete book button click
//function deleteBook(bookId) {
//
//    // Get CSRF token
//    var csrftoken = getCookie('csrftoken');
//
//    // Confirm deletion with the user
//    var confirmDelete = confirm('Are you sure you want to delete this book?');
//
//    if (confirmDelete) {
//        // Send AJAX DELETE request with CSRF token
//        fetch('/api/book/' + bookId + '/', {
//            method: 'DELETE',
//            headers: {
//                'Content-Type': 'application/json',
//                'X-CSRFToken': csrftoken
//            }
//        })
//        .then(response => {
//            if (response.ok) {
//                // Redirect to the book list page or perform any other desired action
//                window.location.href = ''; // Redirect to the home page, adjust the URL as needed
//            } else {
//                console.error('Error deleting book:', response.statusText);
//            }
//        })
//        .catch(error => {
//            console.error('Error sending delete request:', error);
//        });
//    }
//}
//
//// Function to get CSRF token from cookies
//function getCookie(name) {
//    var cookieValue = null;
//    if (document.cookie && document.cookie !== '') {
//        var cookies = document.cookie.split(';');
//        for (var i = 0; i < cookies.length; i++) {
//            var cookie = cookies[i].trim();
//            // Check if the cookie name matches the expected format
//            if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                break;
//            }
//        }
//    }
//    return cookieValue;
//}
//
