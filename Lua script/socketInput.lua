-- Import the socket library to connect to the IRC server
local socket = require("socket.core") 

-- Mapping for commands and button presses
local buttons = {"A","B","X","Y","L","R","start","select","up","left","down","right"}

local keyInput = {}
local buttonIn = {}

--Searches through the message for input button commands
--Returns a list of indices corresponding to which buttons have been pressed
function findInput(message)
    if not prepend then
        prepend = ""
    end
    
    buttonList = {}
    numButtons = 0

    for key,value in pairs(buttons) do
        if string.find(message, value .. 'h') then
            numButtons = numButtons + 1
            buttonList[buttons[key]] = 50
        elseif string.find(message, value) then
            numButtons = numButtons + 1
            buttonList[buttons[key]] = 5
        end
    end

    if numButtons == 0 then
        return nil
    else
        return buttonList
    end

end

--Accepts a list of indices corresponding to the buttons that have been pressed
--Returns a table with button input for the emulator
function setPlayerInput(buttonList)
    for key,value in pairs(buttonList) do
        if value > 0 then
            buttonList[key] = buttonList[key] - 1
            hasKey = true
        else
            hasKey = false
        end

        keyInput[key] = hasKey
    end

    return buttonList
end

------------------MAIN-----------------------------

--[[
testin = 'A'
print(testin)
print(findInput(testin))
--]]

s = socket.tcp()

for key,value in pairs(buttons) do
    keyInput[value] = false
    buttonIn[value] = 0
end

-- Wait for incoming connection from python script
s:bind('localhost', 6667)
s:listen()
pyInput = s:accept()

-- Set the receive command to not block, so that the emulator can advance normally
pyInput:settimeout(0)

while true do
    receive = pyInput:receive('*l')

    if receive then
        -- Set buttons based on the command received
        buttonIn = findInput(receive)
        
        -- End the program, used for debugging
        if string.find(receive, "exit") then
            break
        end

        buttonIn = setPlayerInput(buttonIn)
        print(keyInput)
        joypad.set(1, keyInput)
        emu.frameadvance()
    else
        buttonIn = setPlayerInput(buttonIn)
        joypad.set(1, keyInput)
        emu.frameadvance()
    end

end

s:close()

