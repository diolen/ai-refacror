<?php

class User extends AppModel
{
    public $name = 'User';

    public $belongsTo = [
        'Center'
    ];

    public $hasMany = [
        'UsersCenter'
    ];

    public function getActiveUsers()
    {
        return $this->find('all', [
            'conditions' => [
                'User.active' => 1
            ]
        ]);
    }

    public function createUser($data)
    {
        return $this->save($data);
    }
}