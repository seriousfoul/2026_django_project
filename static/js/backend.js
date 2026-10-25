function deleteData(id, mainType, subType) {
	let msg = '確定進行刪除?';
	if(confirm(msg) == true)
   	location.href = `/backend/${mainType}/${subType}/${id}/delete/`;
}


function changePage(mainType, subType) {
   location.href = `/backend/${mainType}/${subType}/`;
}

function changeIndex(mainType) {
   location.href = `/backend/${mainType}/`;
}