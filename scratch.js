this.showUsers = groupId != undefined && groupId != null && groupId != '' ? false : true;
//IF
//(groupID is not undefined) and 
//(groupID is not null) and 
//(groupID is not emptystring) THEN
// return false ELSE
// return true

//if group ID has some value, then showUsers is false

// if groupID is any of the falsey values, then showUsers is true
// but the code doesnt check for all of javascripts falsey values
// so the code is not correct

//would that be the same?
this.showUsers = !!groupId
//if groupID has some value, then showUsers is true