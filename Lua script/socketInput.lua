-- Import the socket library to connect to the IRC server
local socket = require("socket.core") 

-- Mapping for commands and button presses
buttons = {"A","B","start","select","up","left","down","right"}
buttonCmd = {"a","b","start","select","up","left","down","right"}

local state = {true,false}
local keyInput = {}

function findInput(message,commands, prepend)
    if not prepend then
        prepend = ""
    end
    
    for key,value in pairs(commands) do
        front,back = string.find(message, prepend .. value)
        if back == string.len(message) then
            return key
        end
    end
    
    return nil
end

function setPlayerInput(button, keyInput)
    for key,value in pairs(buttons) do
        if key == button then
            keyInput[value] = true
        else
            keyInput[value] = false
        end
    end
    return keyInput
end

s = socket.tcp()

for key,value in pairs(buttons) do
    keyInput[value] = state[2]
end

-- Connect to the IRC server/channel
s:bind('localhost', 6667)
s:accept()

-- Set the receive command to not block, so that the emulator can advance normally
s:settimeout(0)

while true do
    receive = s:receive('*l')

    if receive then
        -- Reply to ping requests to stay connected to the server
        if string.find(receive, ping) then
            s:send("PONG :" .. string.sub(receive, (string.find(receive, ping) + 6)) .. "\r\n\r\n")
            print("Received PING.  Replied PONG")
        else
            -- Set buttons based on the command received
            local button = findInput(receive, buttonCmd, msg)
            
            -- End the program, used for debugging
            if string.find(receive, msg .. "exit") then
                break
            end

            keyInput = setPlayerInput(button, keyInput)
            joypad.set(1, keyInput)
            emu.frameadvance()
        end
    else
        keyInput = setPlayerInput(button, keyInput)
        joypad.set(1, keyInput)
        emu.frameadvance()
    end

end

s:close()