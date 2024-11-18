// my types for this project.

export type Workout = {
    "id": number;
    "routine": number;
    "name": String;
    "description": String;
    "order": number;
    "exercises": Array<any>;
}

export type Routine = {
    id: number;
    name: String;
    description: String;
    split: String;
    creation_date: String;
    workouts: Array<Workout>;
};