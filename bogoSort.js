let myArr = [1,2,5,4,3];

function bogoSort(arr){
	//function to check if sorted
	var isSorted = function(arr){
		for(var i = 1; i<arr.length; i++){
			if(arr[i-1] > arr[i]){
				return false;
			}
		}
		return true;
	}
	//shuffle
	var shuffle = function(arr){
		var count = arr.length;
		var index;

		while(count>0){
			index = Math.floor(Math.random() * count);
			count --;

			//swap places
			[[arr[index]], arr[count]] = [arr[count], arr[index]]
		}
		return arr;
	}

	var sort = function(arr){
		var sorted = false;
		var count = 0
		while (!sorted){
			count ++;
			arr = shuffle(arr);
			console.log(arr, count)
			sorted = isSorted(arr);
		}
		return arr;
	}
	return sort(arr);
}

