#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (!error) {
    const tasks = JSON.parse(body);
    const Taskscompleted = {};
    tasks.forEach((task) => {
      if (task.completed) {
        if (Taskscompleted[task.userId]) {
          Taskscompleted[task.userId]++;
        } else {
          Taskscompleted[task.userId] = 1;
        }
      }
    });
    console.log(Taskscompleted);
  } else {
    console.error('Error:', error);
  }
});
