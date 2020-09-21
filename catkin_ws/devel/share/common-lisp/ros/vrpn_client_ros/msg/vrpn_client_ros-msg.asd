
(cl:in-package :asdf)

(defsystem "vrpn_client_ros-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Position_Yaw" :depends-on ("_package_Position_Yaw"))
    (:file "_package_Position_Yaw" :depends-on ("_package"))
  ))