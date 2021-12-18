box.cfg {listen = 3301}
box.schema.user.passwd('pass')

queue = box.schema.create_space(
'queue',
{
format = {
{name = "Day", type = 'number'},
{name = "TickTime", type = 'number'},
{name = "Speed", type = 'number'}
}, if_not_exists = true
}
)

queue:create_index('primary',{
parts = {'Day','TickTime','Speed'}
})
queue:create_index('ticktime',{
parts = {'TickTime'},
unique=false,
type='TREE'
})
queue:create_index('speed',{
parts = {'Speed'},
unique=false,
type='TREE'
})

mqtt = require('mqtt')
json = require('json')

connection = mqtt.new("Nikita_Khayrulin", true)

connection:login_set('Hans', 'Test')

connection:connect({host='194.67.112.161', port=1883})

connection:on_message(function (message_id, topic, payload, gos, retain)
newdata = json.decode(payload)
queue:insert({newdata.Day, newdata.TickTime, newdata.Speed})
end)

connection:subscribe('v14')
