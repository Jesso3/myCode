let source = Array.from(document.querySelectorAll('.yt-core-image'))
  .filter(image => {
    const parentLink = image.closest('a'); 
    return parentLink && !parentLink.href.includes('shorts');
  })
  .map(image => image.src)
  .filter(src => src !== "");

  let refs = Array.from(document.querySelectorAll('a'))
  .filter(a => (a.classList.contains('media-item-thumbnail-container') || a.id.includes('thumbnail')) && !a.href.includes('shorts'))
  .map(a => a.href)
  .filter((href, index, self) => href !== "" && href !== null && self.indexOf(href) === index);

let ids = refs.map(ref => (ref.match(/(?<=v=)[^&]+/g) || [])[0])
  .filter(id => id !== undefined);

let titles = Array.from(document.querySelectorAll('span'))
.filter(a => 
  a.classList.contains('yt-core-attributed-string') && 
  a.getAttribute('role') === "text" && 
  a.parentElement.tagName === 'H3' && 
  !a.parentElement.getAttribute('aria-label') 
)
  .map(a => a.innerHTML)

if (titles.length == 0) {
  titles = Array.from(document.querySelectorAll('yt-formatted-string'))
    .filter(a => a.id.includes('video-title'))
    .map(a => a.innerHTML)
}

let minLength = Math.min(source.length, refs.length, ids.length, titles.length);

let combinedObject = {};

for (let i = 0; i < minLength; i++) {
  combinedObject[i] = {
    source: source[i],
    ref: refs[i],
    id: ids[i],
    title: titles[i]
  };
}

console.log(combinedObject);