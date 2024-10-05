let inter = setInterval(() => window.scrollBy(0, 100), 1);
let totalTime = 15000;
let goUp;

setTimeout(() => {
    clearInterval(inter);
    document.querySelectorAll('button[aria-label="Show more"]').forEach(e => e.click());
    goUp = setInterval(() => window.scrollBy(0, -100), 1);
}, totalTime-5000);

setTimeout(() => clearInterval(goUp), totalTime);

setTimeout(() => {

    document.querySelectorAll('button[aria-label="Show more"]').forEach(e => e.click());

    let source = Array.from(document.querySelectorAll('.yt-core-image'))
        .filter(image => {
            const parentLink = image.closest('a');
            return parentLink && !parentLink.href.includes('shorts');
        })
        .map(image => image.src)
        .filter(src => src !== "");

    let refs = Array.from(document.querySelectorAll('a'))
        .filter(a => 
            (a.classList.contains('media-item-thumbnail-container') || a.id.includes('thumbnail')) 
            && !a.href.includes('shorts'))
        .map(a => a.href)
        .filter((href, index, self) => href !== "" && href !== null && self.indexOf(href) === index);

    let ids = refs.map(ref => (ref.match(/(?<=v=)[^&]+/g) || [])[0])
        .filter(id => id !== undefined);

    let titles = Array.from(document.querySelectorAll('span'))
        .filter(a => 
            a.classList.contains('yt-core-attributed-string') && 
            a.getAttribute('role') === "text" && 
            a.parentElement.tagName === 'H3' && 
            !a.parentElement.getAttribute('aria-label'))
        .map(a => a.innerHTML);

    if (titles.length == 0) {
        titles = Array.from(document.querySelectorAll('yt-formatted-string'))
            .filter(a => a.id.includes('video-title'))
            .map(a => a.innerHTML);
    }

    let minLength = Math.min(source.length, refs.length, ids.length, titles.length);

    let combinedObject = {};

    for (let i = 0; i < minLength; i++) {
        combinedObject[i] = {
            source: source[i + source.length-minLength],
            ref: refs[i + refs.length-minLength],
            id: ids[i + ids.length-minLength],
            title: titles[i + titles.length-minLength]
        };
    }

    console.log(combinedObject);
}, totalTime);
