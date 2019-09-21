<?php
class Komen {
    private $mysqli;

    function __construct($conn)
    {
        $this->mysqli = $conn;
    }

    public function tampil($id = null){
        $db = $this->mysqli->conn;
        $sql = "SELECT posts.title, users.username, comments.comment FROM comments, posts, users WHERE users.id = posts.createdBy and comments.postId = posts.id;";
  
        if($id != null){
            $sql .= " WHERE id_brg = $id";
        }
        $query = $db->query($sql) or die ($db->error);
        return $query;
    }

    function __destruct()
    {
        $db = $this->mysqli->conn;
        $db->close();
    }

}

?>