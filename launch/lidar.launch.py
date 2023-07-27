<launch>
  <node name="lidar_node" pkg="urg_node" type="urg_node" output="screen">
    <param name="serial_port" value="/dev/ttyUSB0"/>
    <param name="frame_id" value="lidar_link"/>
    <param name="angle_compensate" value="true"/>
    <param name="scan_mode" value="Standard"/>
  </node>
</launch>
