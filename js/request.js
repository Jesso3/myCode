(async () => {
  console.log(
    await (
      await fetch("https://www.geeksforgeeks.org/node-js-request-module/")
    ).text(),
  );
})();
