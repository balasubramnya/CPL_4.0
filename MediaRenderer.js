var args = Catalyst.script.args() ? JSON.parse(Catalyst.script.args()) : {};
console.log("Arguments for srcvideo: " + args.srcvideo);
console.log("Arguments for transcoder: " + args.transcoder);
//console.log("Arguments for preset :" + args.preset);
//console.log("Arguments for framerate: " + args.framerate);


var transcoder = eval(args.transcoder);
//var preset = eval(args.preset);
//var framerate = eval(args.framerate);

// create empty project
var project = Catalyst.project;
var timeline = project.project.activeTimeline;

// add source video to first track
timeline.newTrack(0);
project.addMediaToTrack(args.srcvideo, 0);

// Get best match preset
var presets    = Catalyst.renderManager.getTranscoderPresets(transcoder);
var matchPreset = Catalyst.renderManager.getBestMatchIndex(transcoder, project, true);
console.log("best preset name" + presets[matchPreset].findById(Catalyst.preset.kName).value);
//var name       = presets[matchPreset].findById(Catalyst.preset.kName).value;

var renderJob = {
    project   : project,
    dest      : args.dest,
    format    : transcoder,
    withPreset: matchPreset,
};
Catalyst.renderManager.render(renderJob, function (job, status) {
    switch (status.message) {
        case Catalyst.message.progress:
            console.log("percentage completed: " + status.percentage);
            break;
    }
});