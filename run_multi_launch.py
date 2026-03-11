from launch import LaunchDescription
from launch_ros.actions import Node
#### add the necessary imports
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution

def generate_launch_description():
#### add the argument declaration
		name_0_arg = DeclareLaunchArgument('my_parameter', default_value = TextSubstitution(text='default'))
####	
	
		talk1 = Node(
							package = 'python_parameters',
							namespace = 'group6',
							executable = 'minimal_param_node',
							name = 'Hiro',
							parameters = [{'my_parameter': 'Hiro'}])
							
		talk2 = Node(
							package = 'python_parameters',
							namespace = 'group6',
							executable = 'minimal_param_node',
							name = 'Baymax',
							parameters = [{'my_parameter': 'Baymax'}],
							arguments = ["--ros-args", "--log-level", "WARN"])
							
		talk3 = Node(
							package = 'python_parameters',
							namespace = 'group0',
							executable = 'minimal_param_node',
							name = 'NA',
							#parameters = [{'my_parameter': 'NA', 'wait_time': 2.5}])
							parameters = [{'my_parameter': LaunchConfiguration('my_parameter'), 'wait_time': 2.5}])
		
		return LaunchDescription([
						name_0_arg,  #argument must also be part of the launch description
						talk1, talk2, talk3])
