function pascalTriangle(n) {
  if (n <= 0) {
    return [];
  }
  
  var triangle = [[1]];
  
  for (var i = 1; i < n; i++) {
    var row = [1];
    var prevRow = triangle[i - 1];
    
    for (var j = 1; j < i; j++) {
      row.push(prevRow[j - 1] + prevRow[j]);
    }
    
    row.push(1);
    triangle.push(row);
  }
  
  return triangle;
}

