// Daniel Shiffman
// Game of Life

function make2DArray(cols, rows) {
  let arr = new Array(cols);
  for (let i = 0; i < arr.length; i++) {
    arr[i] = new Array(rows);
  }
  return arr;
}

let grid;
let cols;
let rows;
let resolution = 4;
let _height = 1;

function setup() {
  createCanvas(1000, 800);
  frameRate(20)
  cols = width / resolution;
  rows = height / resolution;

  grid = make2DArray(cols, rows);
  for (let i = 0; i < cols; i++) {
    for (let j = 0; j < rows; j++) {
      if (i == cols/2 && j == 0){
        grid[i][j] = 1
      }
      else{
        grid[i][j] = 0
      }
    }
  }
}

function draw() {
  background(0);
  _height = getHeight(rows,cols,grid)
  for (let i = 0; i < cols; i++) {
    for (let j = 0; j < rows; j++) {
      let x = i * resolution;
      let y = j * resolution;
      if (grid[i][j] == 1) {
        fill(255);
        stroke(0);
        rect(x, y, resolution - 1, resolution - 1);
      }
    }
  }

  let next = make2DArray(cols, rows);

  // Compute next based on grid
  for (let i = 0; i < cols; i++) {
    for (let j = 1; j < rows; j++) {
      let state = grid[i][j];
      // Count live neighbors!
      let sum = 0;
      let neighbors = countNeighbors(grid, i, j);

      if (neighbors == 0 || neighbors == 3) {
        next[i][j] = 0;
      } else if (neighbors == 1 || neighbors == 2) {
        next[i][j] = 1;
      } else {
        next[i][j] = state;
      }

    }
  }

  grid = next;



}

function getHeight(rows,cols,grid){
  for (let i = 0; i < rows; i++){
    for (let j = 0; j < cols; j++){
      if (grid[j][i] == 1){
        //console.log(i,j,rows)
        return i-1;
      }
    }
  }
}


function countNeighbors(grid, x, y) {
  let sum = 0;
  j = -1
  for (let i = -1; i < 2; i++) {
    let col = (x + i + cols) % cols;
    let row = (y + j + rows) % rows;
    //console.log(x,y,col,row, grid[col][row], _height)
    sum += grid[col][row];   
  }
  //sum -= grid[x][y]
  return sum;
}