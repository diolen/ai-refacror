<?php

class UsersCenter extends AppModel
{
    public $name = 'UsersCenter';

    public $belongsTo = [
        'User',
        'Center'
    ];

    public function linkUserToCenter($userId, $centerId)
    {
        return $this->save([
            'user_id' => $userId,
            'center_id' => $centerId
        ]);
    }
}