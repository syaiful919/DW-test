<?php
include "models/m_komen.php";

$brg = new Komen($connection);

?>
       
       <div class="row">
          <div class="col-lg-12" >
            <h1 align=center >Technical Test DumbWays.id</h1>
            <br>

          </div>
        </div>

        <div class="row">
            <div class="col-lg-12">    
                <div class="table-responsive">
                    <table class="table table-bordered table-hover table-striped">
                        <tr>
                            <th class="text-center">No.</th>
                            <th class="text-center">Title</th>
                            <th class="text-center">Username</th>
                            <th class="text-center">Comments</th>   
                        </tr>    

                        <?php
                        $no = 1;
                        $tampil = $brg->tampil();
                        while($data = $tampil ->fetch_object()){

                        ?>
                        <tr>
                            <td align="center"><?php echo $no++.".";?></td>
                            <td><?php echo $data->title;?></td>
                            <td><?php echo $data->username;?></td>
                            <td><?php echo $data->comment;?></td>
                        </tr>
                        <?php
                        } ?>

                    <table>
                </div>  

            </div>
        </div>

    