let inter = setInterval(() => window.scrollBy(0, 100), 1);
let goUp;

setTimeout(() => {
    clearInterval(inter)
    goUp = setInterval(() => window.scrollBy(0, -100), 1);
}, 10000);
setTimeout(() => clearInterval(goUp),20000)