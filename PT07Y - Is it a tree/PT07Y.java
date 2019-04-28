/*
* Project name : SPOJ: PT07Y - Is it a tree
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-28
* Description  :
* Status       : Accepted (23695543)
* Tags         : java, graph theory, tree graph, connected graph, depth first search, DFS, strict graph
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;

final class Reader{
    final private int BUFFER_SIZE = 1 << 16;
    private DataInputStream dis;
    private byte[] buffer;
    private int bufferPointer, bytesRead;

    public Reader(){
        dis = new DataInputStream(System.in);
        buffer = new byte[BUFFER_SIZE];
        bufferPointer = bytesRead = 0;
    }

    public int nextPositiveInt() throws IOException{
        int ret = 0;
        byte c = read();
        while (c <= ' ')
            c = read();
        do{
            ret = ret * 10 + c - '0';
        }  while ((c = read()) >= '0' && c <= '9');

        return ret;
    }

    private void fillBuffer() throws IOException{
        bytesRead = dis.read(buffer, bufferPointer = 0, BUFFER_SIZE);
        if (bytesRead == -1)
            buffer[0] = -1;
    }

    private byte read() throws IOException{
        if (bufferPointer == bytesRead)
            fillBuffer();
        return buffer[bufferPointer++];
    }

    public void close() throws IOException{
        if (dis == null)
            return;
        dis.close();
    }
}

final class StrictGraph{
  private int order;
  private int size;
  private ArrayList<ArrayList<Integer>> adjacency_lists;
  private boolean[] visited;

  public StrictGraph(){
    this(0, 0);
  }

  public StrictGraph(int graph_order){
    this(graph_order, 0);
  }

  public StrictGraph(int graph_order, int graph_size){
    order = graph_order;
    size = graph_size;
    adjacency_lists = new ArrayList<ArrayList<Integer>>();
    for (int i = 0; i < order; i++){
      adjacency_lists.add(new ArrayList<Integer>());
    }
  }

  public void insertEdge(int v0, int v1){
    adjacency_lists.get(v0).add(v1);
    adjacency_lists.get(v1).add(v0);
  }

  public int getOrder(){
    return order;
  }

  public int getSize(){
    return size;
  }

  private int noOfConnectedVertices(int v){
    visited[v] = true;

    int no_of_connected_vertices = 1;
    for (int i : adjacency_lists.get(v)){
      if (!visited[i]){
         no_of_connected_vertices += noOfConnectedVertices(i);
      }
    }
    return no_of_connected_vertices;
  }

  public boolean isConnected(){
    visited = new boolean[order];

    if (noOfConnectedVertices(0) == order){
      return true;
    } else {
      return false;
    }
  }

  public boolean isTree(){
    if (order == size + 1){
      if (this.isConnected()){
        return true;
      } else {
        return false;
      }
    } else {
      return false;
    }
  }
}

final class PT07Y{
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    int n = r.nextPositiveInt(), m = r.nextPositiveInt();
    StrictGraph SG = new StrictGraph(n, m);

    while (m-- > 0){
      SG.insertEdge(r.nextPositiveInt() - 1, r.nextPositiveInt() - 1);
    }

    if (SG.isTree()){
      System.out.println("YES");
    } else {
      System.out.println("NO");
    }
  }
}
