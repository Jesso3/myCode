const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json());

app.post('/updateWinner', (req, res) => {
  const winnerName = req.body.winner;

  fs.appendFile('winners.txt', `The winner is: ${winnerName}\n`, (err) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Error updating the file.');
    }

    res.send('Winner updated successfully.');
  });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
