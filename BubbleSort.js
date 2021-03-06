// Bubble Sort is an algorithm basically where we have to compare two numbers at a time and then Swap them if they are out of Order.
// i.e In ascending order.
// It works by comparing two adjacent numbers next to each other and then swapping their places if the smaller index's value
// is larger than the larger Index's value.
// And the continues looping through until all values are in order from the smallest to the larger value.

// Example:

function bubbleSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    //cycle through the array items
    for (let j = 0; j < arr.length; j++) {
      //compare adjacent items
      if (arr[j] > arr[j + 1]) {
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}

console.log(bubbleSort([14, 33, 18, 36, 17, 5, 29, 42, 26]));
