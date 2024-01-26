chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'getImages') {
      var images = Array.from(document.images).map(function(img) {
        return img.src;
      });
  
      sendResponse({ images: images });
    }else if (request.action === 'blurImages') {
        blurImages(request.images);
    }
});
    function blurImages(filteredImages) {
      console.log(filteredImages);
      var images = document.images;

      if (Array.isArray(filteredImages)) {
        for (var i = 0; i < images.length; i++) {
          var img = images[i];
          if (filteredImages.includes(img.src)) {
            img.style.filter = 'blur(10px)';
          } else {
            continue;
          }
        }
      } else {
        console.error('Error: filteredImages is not a valid array.');
      }
    }
  