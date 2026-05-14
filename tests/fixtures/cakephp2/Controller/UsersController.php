<?php

class UsersController extends AppController
{
    public $uses = [
        'User',
        'Center',
        'UsersCenter'
    ];

    public function index()
    {
        $users = $this->User->find('all');

        return $users;
    }

    public function add()
    {
        $data = [
            'name' => 'Test User'
        ];

        $this->User->save($data);

        $this->Center->find('first');
    }

    public function assignCenter($userId, $centerId)
    {
        $this->UsersCenter->save([
            'user_id' => $userId,
            'center_id' => $centerId
        ]);

        $this->User->findById($userId);

        $this->Center->findById($centerId);
    }
}