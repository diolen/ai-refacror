<?php

class CentersController extends AppController
{
    public $uses = [
        'Center',
        'User'
    ];

    public function index()
    {
        return $this->Center->find('all');
    }

    public function users($centerId)
    {
        return $this->User->find('all', [
            'conditions' => [
                'User.center_id' => $centerId
            ]
        ]);
    }

    public function create()
    {
        $data = [
            'name' => 'Main Center'
        ];

        return $this->Center->save($data);
    }
}