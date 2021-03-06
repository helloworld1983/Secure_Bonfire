def gen_tb_package(tb_file_name, traffic, sensitive_pir, sensitive_data_source, sensitive_data_destination,  attack, pir, attacker_source, attacker_destination, attacker_packet_length, attacker_pir, seed):
	tb_file = open(tb_file_name, "w")
	tb_file.write("--Copyright (C) 2016 Siavoosh Payandeh Azad\n\n\n\n")
	tb_file.write("--traffic:"+str(traffic)+"\n")
	tb_file.write("--attack: "+str(attack)+"\n")
	tb_file.write("--pir:"+str(pir)+"\n")
	tb_file.write("--sensitive_data_source:"+str(sensitive_data_source)+"\n")
	tb_file.write("--sensitive_data_destination:"+str(sensitive_data_destination)+"\n")
	tb_file.write("--attacker_source:"+str(attacker_source)+"\n")
	tb_file.write("--attacker_destination:"+str(attacker_destination)+"\n")
	tb_file.write("--attacker_packet_length:"+str(attacker_packet_length)+"\n")
	tb_file.write("--attacker_pir:"+str(attacker_pir)+"\n")
	tb_file.write("--seed:"+str(seed)+"\n")
	tb_file.write("\n")
	tb_file.write("library ieee;\n")
	tb_file.write("use ieee.std_logic_1164.all;\n")
	tb_file.write("use ieee.std_logic_unsigned.all;\n")
	tb_file.write("use IEEE.NUMERIC_STD.all;\n")
	tb_file.write("use ieee.math_real.all;\n")
	tb_file.write("use std.textio.all;\n")
	tb_file.write("use ieee.std_logic_misc.all;\n")
	tb_file.write("\n")
	tb_file.write("package TB_Package is\n")
	tb_file.write("   function CX_GEN(current_address, network_x, network_y : integer) return integer;\n")
	tb_file.write("\n")
	tb_file.write("   procedure NI_control(network_x, network_y, frame_length, current_address, initial_delay, min_packet_size, max_packet_size: in integer;\n")
	tb_file.write("                      finish_time: in time;\n")
	tb_file.write("                      APP_FILE_NAME: in string;\n")
	tb_file.write("                      signal clk:                      in std_logic;\n")
	tb_file.write("                      -- NI configuration\n")
	tb_file.write("                      signal reserved_address :        in std_logic_vector(29 downto 0);\n")
	tb_file.write("                      signal flag_address :            in std_logic_vector(29 downto 0) ; -- reserved address for the memory mapped I/O\n")
	tb_file.write("                      signal counter_address :         in std_logic_vector(29 downto 0);\n")
	tb_file.write("                      signal reconfiguration_address : in std_logic_vector(29 downto 0);  -- reserved address for reconfiguration register\n")
	tb_file.write("                      -- NI signals\n")
	tb_file.write("                      signal enable:                   out std_logic;\n")
	tb_file.write("                      signal write_byte_enable:        out std_logic_vector(3 downto 0);\n")
	tb_file.write("                      signal address:                  out std_logic_vector(31 downto 2);\n")
	tb_file.write("                      signal data_write:               out std_logic_vector(31 downto 0);\n")
	tb_file.write("                      signal data_read:                in std_logic_vector(31 downto 0);\n")
	tb_file.write("                      signal test:                out std_logic_vector(31 downto 0));\n")
	tb_file.write("\n")
	tb_file.write("end TB_Package;\n")
	tb_file.write("\n")
	tb_file.write("package body TB_Package is\n")
	tb_file.write("  constant Header_type : std_logic_vector := \"001\";\n")
	tb_file.write("  constant Body_type : std_logic_vector := \"010\";\n")
	tb_file.write("  constant Tail_type : std_logic_vector := \"100\";\n")
	tb_file.write("  constant MaxMemoryAddress1 : integer := 4095; -- should fit in 12 bits (smaller than 4096)\n")
	tb_file.write("  constant MaxMemoryAddress2 : integer := 1048575; -- should fit in 20 bits (smaller than 1048576)\n")
	tb_file.write("\n")
	tb_file.write("  function CX_GEN(current_address, network_x, network_y: integer) return integer is\n")
	tb_file.write("    variable X, Y : integer := 0;\n")
	tb_file.write("    variable CN, CE, CW, CS : std_logic := '0';\n")
	tb_file.write("    variable CX : std_logic_vector(3 downto 0);\n")
	tb_file.write("  begin\n")
	tb_file.write("    X :=  current_address mod  network_x;\n")
	tb_file.write("    Y :=  current_address / network_x;\n")
	tb_file.write("\n")
	tb_file.write("    if X /= 0 then\n")
	tb_file.write("      CW := '1';\n")
	tb_file.write("    end if;\n")
	tb_file.write("\n")
	tb_file.write("    if X /= network_x-1 then\n")
	tb_file.write("      CE := '1';\n")
	tb_file.write("    end if;\n")
	tb_file.write("\n")
	tb_file.write("    if Y /= 0 then\n")
	tb_file.write("      CN := '1';\n")
	tb_file.write("    end if;\n")
	tb_file.write("\n")
	tb_file.write("    if Y /= network_y-1 then\n")
	tb_file.write("     CS := '1';\n")
	tb_file.write("    end if;\n")
	tb_file.write("   CX := CS&CW&CE&CN;\n")
	tb_file.write("   return to_integer(unsigned(CX));\n")
	tb_file.write("  end CX_GEN;\n")
	tb_file.write("\n")
	tb_file.write("  procedure NI_control(network_x, network_y, frame_length, current_address, initial_delay, min_packet_size, max_packet_size: in integer;\n")
	tb_file.write("                      finish_time: in time;\n")
	tb_file.write("                      APP_FILE_NAME: in string;\n")
	tb_file.write("                      signal clk:                      in std_logic;\n")
	tb_file.write("                      -- NI configuration\n")
	tb_file.write("                      signal reserved_address :        in std_logic_vector(29 downto 0);\n")
	tb_file.write("                      signal flag_address :            in std_logic_vector(29 downto 0) ; -- reserved address for the memory mapped I/O\n")
	tb_file.write("                      signal counter_address :         in std_logic_vector(29 downto 0);\n")
	tb_file.write("                      signal reconfiguration_address : in std_logic_vector(29 downto 0);  -- reserved address for reconfiguration register\n")
	tb_file.write("                      -- NI signals\n")
	tb_file.write("                      signal enable:                   out std_logic;\n")
	tb_file.write("                      signal write_byte_enable:        out std_logic_vector(3 downto 0);\n")
	tb_file.write("                      signal address:                  out std_logic_vector(31 downto 2);\n")
	tb_file.write("                      signal data_write:               out std_logic_vector(31 downto 0);\n")
	tb_file.write("                      signal data_read:                in std_logic_vector(31 downto 0);\n")
	tb_file.write("                      signal test:                     out std_logic_vector(31 downto 0)) is\n")
	tb_file.write("    -- variables for random functions\n")
	tb_file.write("    constant DATA_WIDTH : integer := 32;\n")
	tb_file.write("    variable seed1 :positive := current_address+"+str(seed)+";\n")
	tb_file.write("    variable seed2 :positive := current_address+"+str(seed)+";\n")
	tb_file.write("    variable rand : real ;\n")
	tb_file.write("    --file handling variables\n")
	tb_file.write("    variable SEND_LINEVARIABLE : line;\n")
	tb_file.write("    file SEND_FILE : text;\n")
	tb_file.write("\n")
	tb_file.write("    variable APP_LINEVARIABLE : line;\n")
	tb_file.write("    file APP_FILE : text;\n")
	tb_file.write("    variable packet_info : integer;\n")
	tb_file.write("    variable gen_time: time;\n")
	tb_file.write("\n")
	tb_file.write("    -- sending variables\n")
	tb_file.write("    variable send_destination_node, send_counter, send_id_counter: integer:= 0;\n")
	tb_file.write("    variable send_packet_length: integer:= 8;\n")
	tb_file.write("    variable Mem_address_1, Mem_address_2, RW, DI, ROLE, OPCODE: integer := 0;\n")
	tb_file.write("    type state_type is (Idle, Header_flit, Body_flit, Body_flit_1, Tail_flit);\n")
	tb_file.write("    variable  state : state_type;\n")
	tb_file.write("\n")
	tb_file.write("    variable  frame_starting_delay : integer:= 0;\n")
	tb_file.write("    variable  frame_length_mod : integer:= 0;\n")
	tb_file.write("    variable frame_counter: integer:= 0;\n")
	tb_file.write("    variable packet_gen_time: time;\n")
	tb_file.write("    variable sent: boolean := True;\n")
	tb_file.write("    variable packet_sent: boolean := False;\n")
	tb_file.write("\n")
	tb_file.write("    begin\n")
	tb_file.write("\n")
	tb_file.write("    file_open(SEND_FILE,\"sent.txt\",WRITE_MODE);\n")
	tb_file.write("\n")
	tb_file.write("    if APP_FILE_NAME = \"NONE\" then\n")
	tb_file.write("      report \"no app file given!\";\n")
	tb_file.write("    else\n")
	tb_file.write("      file_open(APP_FILE, APP_FILE_NAME, READ_MODE);\n")
	tb_file.write("    end if;\n")
	tb_file.write("\n")



#        tb_file.write("\n\n\n")
#        tb_file.write("--defining the frame_length\n")
# 
#        if attack:
#                tb_file.write("if current_address = "+str(attacker_source)+" then\n")
#                attack_pir_rate = int(pir/float(attacker_pir))
#                if attack_pir_rate >= 1:
#                        tb_file.write("  frame_length_mod := frame_length*"+str(attack_pir_rate)+";\n")
#                else:
#                        tb_file.write("  frame_length_mod := frame_length/"+str(int(float(attacker_pir)/pir))+";\n")
#                tb_file.write("else\n")
#
#        tb_file.write("  frame_length_mod := frame_length;\n")
#
#        if attack:
#                tb_file.write("end if;   \n")
#        tb_file.write("\n\n\n")


#--defining the frame_length
#if current_address = 9 then
#  frame_length_mod := frame_length/6;
#else
#  frame_length_mod := frame_length;
#end if;


#        tb_file.write("\n\n")
#        tb_file.write("-- Defining the time frame length\n")
#
#
#        tb_file.write("if current_address = "+str(sensitive_data_source)+" then -- setting the sensitive PIR\n")
#        sensitive_pir_rate = int(pir/float(sensitive_pir))
#        if sensitive_pir_rate >= 1:
#            tb_file.write("  frame_length_mod := frame_length*"+str(sensitive_pir_rate)+";\n")
#        else:
#            tb_file.write("  frame_length_mod := frame_length/"+str(int(float(sensitive_pir)/pir))+";\n")
#        if attack:
#            tb_file.write("elsif current_address = "+str(attacker_source)+" then -- setting the attacker PIR\n")
#            attack_pir_rate = int(pir/float(attacker_pir))
#            if attack_pir_rate >= 1:
#                tb_file.write("  frame_length_mod := frame_length*"+str(attack_pir_rate)+";\n")
#            else:
#                tb_file.write("  frame_length_mod := frame_length/"+str(int(float(attacker_pir)/pir))+";\n")
#        tb_file.write("else -- setting the network PIR\n")
#        tb_file.write("    frame_length_mod := frame_length;\n")
#        tb_file.write("end if;\n")



        tb_file.write("\n\n")
        tb_file.write("-- Defining the time frame length\n")


        tb_file.write("if current_address = "+str(sensitive_data_source)+" then -- setting the sensitive PIR\n")
        tb_file.write("  frame_length_mod := "+str(int(1/sensitive_pir))+";\n")
      
        if attack:
           tb_file.write("elsif current_address = "+str(attacker_source)+" then -- setting the attacker PIR\n")
           tb_file.write("  frame_length_mod := "+str(int(1/attacker_pir))+";\n")
           
        tb_file.write("else -- setting the network PIR\n")
        tb_file.write("    frame_length_mod := frame_length;\n")
        tb_file.write("end if;\n")



#        if attack or traffic:
#            tb_file.write("    if current_address = "+str(sensitive_data_source)+" then\n  ")

#        tb_file.write("    frame_length_mod := frame_length;\n")

#        if attack and traffic:
#            tb_file.write("    elsif current_address = "+str(attacker_source)+" then\n")
#        elif attack or traffic:
#            tb_file.write("    else\n")            

#        if attack:            
#            attack_pir_rate = int(sensitive_pir/float(attacker_pir))
#            if attack_pir_rate >= 1:
#                tb_file.write("      frame_length_mod := frame_length*"+str(attack_pir_rate)+";\n")
#            else:
#                tb_file.write("      frame_length_mod := frame_length/"+str(int(float(attacker_pir)/sensitive_pir))+";\n")

#        if attack and traffic:
#            tb_file.write("    else\n")

#        if traffic:
#            traffic_pir_rate = int(sensitive_pir/float(pir))
#            if traffic_pir_rate >= 1:
#                tb_file.write("      frame_length_mod := frame_length*"+str(traffic_pir_rate)+";\n")
#            else:
#                tb_file.write("      frame_length_mod := frame_length/"+str(int(float(pir)/sensitive_pir))+";\n")

#        if attack or traffic:
#            tb_file.write("   end if;\n")

	tb_file.write("\n\n")


	tb_file.write("\n")
	tb_file.write("    enable <= '1';\n")
	tb_file.write("    state :=  Idle;\n")
	tb_file.write("    send_packet_length := min_packet_size;\n")
	tb_file.write("    uniform(seed1, seed2, rand);\n")
	tb_file.write("    frame_starting_delay := integer(((integer(rand*100.0)*(frame_length_mod - max_packet_size-1)))/100);\n")
	tb_file.write("\n")
	tb_file.write("    wait until clk'event and clk ='0';\n")
	tb_file.write("    address <= reconfiguration_address;\n")
	tb_file.write("    wait until clk'event and clk ='0';\n")
	tb_file.write("    write_byte_enable <= \"1111\";\n")
	tb_file.write("\n")
	tb_file.write("    data_write <= \"00000000000000000000\" & std_logic_vector(to_unsigned(CX_GEN(current_address, network_x, network_y), 4)) & std_logic_vector(to_unsigned(60, 8));\n")
	tb_file.write("\n")
	tb_file.write("    wait until clk'event and clk ='0';\n")
	tb_file.write("    write_byte_enable <= \"0000\";\n")
	tb_file.write("    data_write <= (others =>'0');\n")
	tb_file.write("\n")
	tb_file.write("    while true loop\n")
	tb_file.write("      -- read the flag status\n")
	tb_file.write("      address <= flag_address;\n")
	tb_file.write("      write_byte_enable <= \"0000\";\n")
	tb_file.write("      wait until clk'event and clk ='0';\n")
	tb_file.write("      frame_counter := frame_counter + 1;\n")
	tb_file.write("      if frame_counter = frame_length_mod then\n")
	tb_file.write("          frame_counter := 0;\n")
	tb_file.write("          packet_sent := False;\n")
	tb_file.write("          uniform(seed1, seed2, rand);\n")
	tb_file.write("          frame_starting_delay := integer(((integer(rand*100.0)*(frame_length_mod - max_packet_size)))/100);\n")
	tb_file.write("      end if;\n")
	tb_file.write("\n")
	tb_file.write("      --flag register is organized like this:\n")
	tb_file.write("      --       .-------------------------------------------------.\n")
	tb_file.write("      --       | N2P_empty | P2N_full |                       ...|\n")
	tb_file.write("      --       '-------------------------------------------------'\n")
	tb_file.write("\n")
	tb_file.write("      if data_read(31) = '0' then  -- N2P is not empty, can receive flit\n")
	tb_file.write("          -- read the received data status\n")
	tb_file.write("          address <= reserved_address;\n")
	tb_file.write("          write_byte_enable <= \"0000\";\n")
	tb_file.write("          wait until clk'event and clk ='0';\n")
	tb_file.write("          frame_counter := frame_counter + 1;\n")
	tb_file.write("          if frame_counter = frame_length_mod then\n")
	tb_file.write("              frame_counter := 0;\n")
	tb_file.write("              packet_sent := False;\n")
	tb_file.write("              uniform(seed1, seed2, rand);\n")
	tb_file.write("              frame_starting_delay := integer(((integer(rand*100.0)*(frame_length_mod - max_packet_size)))/100);\n")
	tb_file.write("          end if;\n")
	tb_file.write("          \n")
	tb_file.write("--defining the traffic\n")
	if traffic:
		tb_file.write("      elsif data_read(30) = '0' then\n")
	else:
		if  attack:
				tb_file.write("      -- no traffic, yes attack\n")
				tb_file.write("      elsif data_read(30) = '0' and (current_address = "+str(sensitive_data_source)+" or current_address = "+str(attacker_source)+") then\n")
		else:
			tb_file.write("      -- no traffic, no attack\n")
			tb_file.write("      elsif data_read(30) = '0' and current_address = "+str(sensitive_data_source)+" then\n")

	tb_file.write("\n")
	tb_file.write("          if APP_FILE_NAME = \"NONE\" then\n")
	tb_file.write("            if frame_counter >= frame_starting_delay  then\n")
	tb_file.write("                if state = Idle and now  < finish_time and packet_sent = False then\n")
	tb_file.write("                      packet_sent := True;\n")
	tb_file.write("                      state :=  Header_flit;\n")
	tb_file.write("                        --send_counter := send_counter+1;\n")
	tb_file.write("                        --generating the packet length\n")
	tb_file.write("                        uniform(seed1, seed2, rand);\n")
	tb_file.write("                        send_packet_length := integer((integer(rand*100.0)*frame_length_mod)/300);\n")
	tb_file.write("                        if (send_packet_length < min_packet_size) then\n")
	tb_file.write("                            send_packet_length:=min_packet_size;\n")
	tb_file.write("                        end if;\n")
	tb_file.write("                        if (send_packet_length > max_packet_size) then\n")
	tb_file.write("                            send_packet_length:=max_packet_size;\n")
	tb_file.write("                        end if;\n")
	tb_file.write("                        -- generating the destination address\n")
	tb_file.write("                        if current_address = "+str(sensitive_data_source)+" then    -- Fixes the destinantion of 12's out going traffic\n")
	tb_file.write("                            send_destination_node := "+str(sensitive_data_destination)+";\n")
	tb_file.write("--defining the attacker's destination and packet length\n")
	if attack:
		tb_file.write("                        elsif current_address = "+str(attacker_source)+" then\n")
		tb_file.write("                            send_destination_node := "+str(attacker_destination)+";\n")
		tb_file.write("                            send_packet_length := "+str(attacker_packet_length)+";\n")
	else:
		tb_file.write("--no attack\n")
	tb_file.write("                        else\n")
	tb_file.write("                          uniform(seed1, seed2, rand);\n")
	tb_file.write("                          send_destination_node := integer(rand*real((network_x*network_y)-1));\n")
	tb_file.write("                          while (send_destination_node = current_address) loop\n")
	tb_file.write("                              uniform(seed1, seed2, rand);\n")
	tb_file.write("                              send_destination_node := integer(rand*real((network_x*network_y)-1));\n")
	tb_file.write("                          end loop;\n")
	tb_file.write("                        end if;\n")
	tb_file.write("                        uniform(seed1, seed2, rand);\n")
	tb_file.write("                        Mem_address_1:= integer(rand*real(MaxMemoryAddress1));\n")
	tb_file.write("\n")
	tb_file.write("                        -- this is body 1\n")
	tb_file.write("                        uniform(seed1, seed2, rand);\n")
	tb_file.write("                        RW := integer(rand*real(2));\n")
	tb_file.write("                        if RW > 1 then\n")
	tb_file.write("                          RW := 1;\n")
	tb_file.write("                        end if;\n")
	tb_file.write("                        uniform(seed1, seed2, rand);\n")
	tb_file.write("                        DI := integer(rand*real(2));\n")
	tb_file.write("                        if DI > 1 then\n")
	tb_file.write("                          DI := 1;\n")
	tb_file.write("                        end if;\n")
	tb_file.write("                        uniform(seed1, seed2, rand);\n")
	tb_file.write("                        ROLE := integer(rand*real(2));\n")
	tb_file.write("                        if ROLE > 1 then\n")
	tb_file.write("                          ROLE := 1;\n")
	tb_file.write("                        end if;\n")
	tb_file.write("                        uniform(seed1, seed2, rand);\n")
	tb_file.write("                        Mem_address_2 := integer(rand*real(MaxMemoryAddress2));\n")
	tb_file.write("\n")
	tb_file.write("                      -- this is the header flit\n")
	tb_file.write("                      packet_gen_time :=  now;\n")
	tb_file.write("                      address <= reserved_address;\n")
	tb_file.write("                      write_byte_enable <= \"1111\";\n")
	tb_file.write("                      data_write <= \"0010\" &  std_logic_vector(to_unsigned(current_address/network_x, 4)) & std_logic_vector(to_unsigned(current_address mod network_x, 4)) & std_logic_vector(to_unsigned(send_destination_node/network_x, 4)) & std_logic_vector(to_unsigned(send_destination_node mod network_x, 4))&std_logic_vector(to_unsigned(Mem_address_1, 12));\n")
	tb_file.write("                      write(SEND_LINEVARIABLE, \"Packet generated at \" & time'image(packet_gen_time) & \" From \" & integer'image(current_address) & \" to \" & integer'image(send_destination_node) &\n")
	tb_file.write("                            \" with length: \"& integer'image(send_packet_length)  & \" id: \" & integer'image(send_id_counter) & \" Mem_address_1: \" & integer'image(Mem_address_1)&\n")
	tb_file.write("                            \" Mem_address_2: \" & integer'image(Mem_address_2) & \" RW: \" & integer'image(RW) & \" DI: \" & integer'image(DI) & \" ROLE: \" & integer'image(ROLE));\n")
	tb_file.write("                      writeline(SEND_FILE, SEND_LINEVARIABLE);\n")
	tb_file.write("                elsif state = Header_flit then\n")
	tb_file.write("                    -- first body flit\n")
	tb_file.write("                    address <= reserved_address;\n")
	tb_file.write("                    write_byte_enable <= \"1111\";\n")
	tb_file.write("                    data_write <= \"0100\" &  std_logic_vector(to_unsigned(Mem_address_2, 20)) & std_logic_vector(to_unsigned(RW,1)) & std_logic_vector(to_unsigned(DI,1)) & std_logic_vector(to_unsigned(ROLE,1)) & std_logic_vector(to_unsigned(OPCODE, 5));\n")
	tb_file.write("                    --send_counter := send_counter+1;\n")
	tb_file.write("                    state :=  Body_flit_1;\n")
	tb_file.write("\n")
	tb_file.write("                elsif state = Body_flit_1 then\n")
	tb_file.write("                    -- the 2nd body flit\n")
	tb_file.write("                    address <= reserved_address;\n")
	tb_file.write("                    write_byte_enable <= \"1111\";\n")
	tb_file.write("                    data_write <= \"0100\" &  std_logic_vector(to_unsigned(send_packet_length, 14)) & std_logic_vector(to_unsigned(send_id_counter, 14));\n")
	tb_file.write("                    --send_counter := send_counter+1;\n")
	tb_file.write("                    --if send_counter = send_packet_length-1 then\n")
	tb_file.write("                    --    state :=  Tail_flit;\n")
	tb_file.write("                    --else\n")
	tb_file.write("                        state :=  Body_flit;\n")
	tb_file.write("                    --end if;\n")
	tb_file.write("                elsif state = Body_flit then\n")
	tb_file.write("                    -- rest of body flits\n")
	tb_file.write("                    address <= reserved_address;\n")
	tb_file.write("                    write_byte_enable <= \"1111\";\n")
	tb_file.write("                    send_counter := send_counter+1;\n")
	tb_file.write("                    if send_counter = send_packet_length+1 then\n")
	tb_file.write("                         data_write <= \"1110\" & \"0000010101000101010001010100\";\n")
	tb_file.write("                        state :=  Tail_flit;\n")
	tb_file.write("                    else\n")
	tb_file.write("                        data_write <= \"0100\" & std_logic_vector(to_unsigned(integer(rand*1000.0), 28));\n")
	tb_file.write("                        state :=  Body_flit;\n")
	tb_file.write("                    end if;\n")
	tb_file.write("                elsif state = Tail_flit then\n")
	tb_file.write("                    -- tail flit\n")
	tb_file.write("                    address <= reserved_address;\n")
	tb_file.write("                    write_byte_enable <= \"1111\";\n")
	tb_file.write("                    --data_write <= \"0100\" & std_logic_vector(to_unsigned(integer(rand*1000.0), 28));\n")
	tb_file.write("                    data_write <=  \"1000\" & \"0000000000000000000000000000\";\n")
	tb_file.write("                    send_counter := 0;\n")
	tb_file.write("                    state :=  Idle;\n")
	tb_file.write("                    send_id_counter := send_id_counter + 1;\n")
	tb_file.write("                    if send_id_counter = 16384 then\n")
	tb_file.write("                      send_id_counter := 0;\n")
	tb_file.write("                    end if;\n")
	tb_file.write("                end if;\n")
	tb_file.write("              end if;\n")
	tb_file.write("\n")
	tb_file.write("              frame_counter := frame_counter + 1;\n")
	tb_file.write("              if frame_counter = frame_length_mod then\n")
	tb_file.write("                  frame_counter := 0;\n")
	tb_file.write("                  packet_sent := False;\n")
	tb_file.write("                  uniform(seed1, seed2, rand);\n")
	tb_file.write("                  frame_starting_delay := integer(((integer(rand*100.0)*(frame_length_mod - max_packet_size)))/100);\n")
	tb_file.write("              end if;\n")
	tb_file.write("          ----------------------------------------------------------------------------\n")
	tb_file.write("          -- Reading from file\n")
	tb_file.write("          else\n")
	tb_file.write("            if sent = True and not endfile(APP_FILE) then\n")
	tb_file.write("              readline (APP_FILE, APP_LINEVARIABLE);\n")
	tb_file.write("              read (APP_LINEVARIABLE, gen_time);\n")
	tb_file.write("              read (APP_LINEVARIABLE, packet_info);\n")
	tb_file.write("              send_destination_node := integer(packet_info);\n")
	tb_file.write("              read (APP_LINEVARIABLE, packet_info);\n")
	tb_file.write("              send_packet_length := integer(packet_info);\n")
	tb_file.write("              read (APP_LINEVARIABLE, packet_info);\n")
	tb_file.write("              Mem_address_1 := integer(packet_info);\n")
	tb_file.write("              read (APP_LINEVARIABLE, packet_info);\n")
	tb_file.write("              Mem_address_2 := integer(packet_info);\n")
	tb_file.write("              read (APP_LINEVARIABLE, packet_info);\n")
	tb_file.write("              RW := integer(packet_info);\n")
	tb_file.write("              read (APP_LINEVARIABLE, packet_info);\n")
	tb_file.write("              DI := integer(packet_info);\n")
	tb_file.write("              read (APP_LINEVARIABLE, packet_info);\n")
	tb_file.write("              ROLE := integer(packet_info);\n")
	tb_file.write("              sent := False;\n")
	tb_file.write("            end if;\n")
	tb_file.write("\n")
	tb_file.write("            --if state = Idle and now  < finish_time and sent = False then\n")
	tb_file.write("            if state = Idle and now >= gen_time and sent = False then\n")
	tb_file.write("                send_counter := send_counter+1;\n")
	tb_file.write("                state :=  Header_flit;\n")
	tb_file.write("                address <= reserved_address;\n")
	tb_file.write("                write_byte_enable <= \"1111\";\n")
	tb_file.write("                packet_gen_time :=  now;\n")
	tb_file.write("                data_write <= \"0000\" &  std_logic_vector(to_unsigned(current_address/network_x, 4)) & std_logic_vector(to_unsigned(current_address mod network_x, 4)) & std_logic_vector(to_unsigned(send_destination_node/network_x, 4)) & std_logic_vector(to_unsigned(send_destination_node mod network_x, 4))&std_logic_vector(to_unsigned(Mem_address_1, 12));\n")
	tb_file.write("                write(SEND_LINEVARIABLE, \"Packet generated at \" & time'image(packet_gen_time) & \" From \" & integer'image(current_address) & \" to \" & integer'image(send_destination_node) &\n")
	tb_file.write("                      \" with length: \"& integer'image(send_packet_length)  & \" id: \" & integer'image(send_id_counter) & \" Mem_address_1: \" & integer'image(Mem_address_1)&\n")
	tb_file.write("                      \" Mem_address_2: \" & integer'image(Mem_address_2) & \" RW: \" & integer'image(RW) & \" DI: \" & integer'image(DI) & \" ROLE: \" & integer'image(ROLE));\n")
	tb_file.write("                writeline(SEND_FILE, SEND_LINEVARIABLE);\n")
	tb_file.write("            elsif state = Header_flit then\n")
	tb_file.write("                address <= reserved_address;\n")
	tb_file.write("                write_byte_enable <= \"1111\";\n")
	tb_file.write("                data_write <= \"0000\" &  std_logic_vector(to_unsigned(Mem_address_2, 20)) & std_logic_vector(to_unsigned(RW,1)) & std_logic_vector(to_unsigned(DI,1)) & std_logic_vector(to_unsigned(ROLE,1)) & std_logic_vector(to_unsigned(OPCODE, 5));\n")
	tb_file.write("                send_counter := send_counter+1;\n")
	tb_file.write("                state :=  Body_flit_1;\n")
	tb_file.write("            elsif state = Body_flit_1 then\n")
	tb_file.write("                address <= reserved_address;\n")
	tb_file.write("                write_byte_enable <= \"1111\";\n")
	tb_file.write("                data_write <= \"0000\" &  std_logic_vector(to_unsigned(send_packet_length, 14)) & std_logic_vector(to_unsigned(send_id_counter, 14));\n")
	tb_file.write("                send_counter := send_counter+1;\n")
	tb_file.write("                if send_counter = send_packet_length-1 then\n")
	tb_file.write("                    state :=  Tail_flit;\n")
	tb_file.write("                else\n")
	tb_file.write("                    state :=  Body_flit;\n")
	tb_file.write("                end if;\n")
	tb_file.write("            elsif state = Body_flit then\n")
	tb_file.write("              address <= reserved_address;\n")
	tb_file.write("              write_byte_enable <= \"1111\";\n")
	tb_file.write("              data_write <= \"0000\" & std_logic_vector(to_unsigned(integer(rand*1000.0), 28));\n")
	tb_file.write("              send_counter := send_counter+1;\n")
	tb_file.write("              if send_counter = send_packet_length-1 then\n")
	tb_file.write("                  state :=  Tail_flit;\n")
	tb_file.write("              else\n")
	tb_file.write("                  state :=  Body_flit;\n")
	tb_file.write("              end if;\n")
	tb_file.write("            elsif state = Tail_flit then\n")
	tb_file.write("              send_counter := 0;\n")
	tb_file.write("              sent := True;\n")
	tb_file.write("              state :=  Idle;\n")
	tb_file.write("              address <= reserved_address;\n")
	tb_file.write("              write_byte_enable <= \"1111\";\n")
	tb_file.write("              data_write <= (others =>'0');\n")
	tb_file.write("              --data_write <= \"0000\" & std_logic_vector(to_unsigned(integer(rand*1000.0), 28));\n")
	tb_file.write("              send_id_counter := send_id_counter + 1;\n")
	tb_file.write("              if send_id_counter = 16384 then\n")
	tb_file.write("                send_id_counter := 0;\n")
	tb_file.write("              end if;\n")
	tb_file.write("            end if;\n")
	tb_file.write("\n")
	tb_file.write("          end if;\n")
	tb_file.write("\n")
	tb_file.write("          wait until clk'event and clk ='0';\n")
	tb_file.write("\n")
	tb_file.write("      end if;\n")
	tb_file.write("\n")
	tb_file.write("\n")
	tb_file.write("    end loop;\n")
	tb_file.write("    file_close(SEND_FILE);\n")
	tb_file.write("  end NI_control;\n")
	tb_file.write("\n")
	tb_file.write("\n")
	tb_file.write("end TB_Package;\n")
	tb_file.close()
	return None
