function deleteData(id, mainType, subType) {
   location.href = `/backend/${mainType}/${subType}/${id}/delete/`;
}


function changePage(mainType, subType) {
   location.href = `/backend/${mainType}/${subType}/`;
}

function changeIndex(mainType) {
   location.href = `/backend/${mainType}/`;
}