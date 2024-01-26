document.addEventListener('DOMContentLoaded', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      chrome.tabs.sendMessage(tabs[0].id, { action: 'getImages' }, function(response) {
        if (response && response.images) {
          displayImageURLs(response.images);
          sendImagesToServer(response.images);
        } else {
          console.error('Error: Unable to get images from content script.');
        }
      });
    });
  

    function sendImagesToServer(images) {
        // Adjust the server URL as needed
        var serverUrl = 'http://127.0.0.1:5000/upload_images';
    
        fetch(serverUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ images: images }),
        })
          .then(response => response.json())
          .then(data => {
            console.log('Server response:', data)
            if (data.filteredImages && Array.isArray(data.filteredImages)){
              blurImagesOnPage(data.filteredImages)
            } else {
              console.error('Error: Invalid server response format.');
            }
        })
          .catch(error => console.error('Error sending images to server:', error));
      }


    function displayImageURLs(images) {
      var imageList = document.getElementById('imageList');
      if (imageList) {
        images.forEach(function(image) {
          var li = document.createElement('li');
          li.textContent = image;
          imageList.appendChild(li);
        });
      } else {
        console.error('Error: Unable to find element with id "imageList".');
      }
    }

    function blurImagesOnPage(filteredImages) {
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
          chrome.tabs.sendMessage(tabs[0].id, { action: 'blurImages', images: filteredImages });
        });
      }

  });
  