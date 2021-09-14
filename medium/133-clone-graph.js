
  // Definition for a Node.
  function Node(val, neighbors) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
 };

/**
* @param {Node} node
* @return {Node}
*/
var cloneGraph = function(node) {
   
   let newNode = new Node(node.val, []);
   console.log(newNode);
   
   if (node.neighbors === [] ) {
       newNode.neighbors = [];
       return newNode;
   } else {
       for(let i = 0; i < node.neighbors.length; i++) {
           newNode.neighbors[i] = cloneGraph(node.neighbors[i]);
       }
   }
   
   return newNode
   
};