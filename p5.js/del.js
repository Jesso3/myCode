let cols = 5;
let rows = 2;

function make2DArray(cols, rows) {
  let arr = new Array(rows);
  for (let i = 0; i < rows; i++) {
    arr[i] = new Array(cols);
  }
  return arr;
}


function moveUp(grids){

  let _new = make2DArray(cols, rows); 
  for(let i = 0; i < rows-1; i++){
    for (let j = 0; j < cols; j++){
      _new[i][j] = grids[i+1][j];  
    }
    
  }
  return _new;
}


arr = [[1,2,3,4,5],
        [6,7,8,9,10]]

console.log(arr[1][3])

console.log(moveUp(arr))