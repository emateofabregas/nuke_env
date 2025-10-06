import nuke

def nodeDefaultsStartup():
    # TIME
    nuke.knobDefault("FrameRange.label", "<b> [value first_frame] - [value last_frame]")
    nuke.knobDefault("TimeBlur.shutteroffset", "centered")
    nuke.knobDefault("Retime.before", "continue")
    nuke.knobDefault("Retime.after", "continue")
    nuke.knobDefault("Retime.filter", "nearest")
    nuke.knobDefault("Retime.label", "<b> speed: [value speed]")

    # CHANNELS
    nuke.knobDefault("Remove.operation", "keep")
    nuke.knobDefault("Remove.channels", "rgba")
    nuke.knobDefault("Shuffle2.label", "<b> [value in1]")
    nuke.knobDefault("Shuffle.label", "<b> [value in]")

    # COLOR CORRECT
    nuke.knobDefault("Grade.label", "<b> mix: [value mix]")
    nuke.knobDefault("ColorCorrect.label", "<b> mix: [value mix]")
    nuke.knobDefault("EXPTool.label", "<b> fStop: [value red]")
    nuke.knobDefault("EXPTool.mode", "0")
    nuke.knobDefault("Gamma.channels", "rgb")
    nuke.knobDefault("Multiply.channels", "rgb")
    nuke.knobDefault("Multiply.label", "<b> mix: [value mix]")
    nuke.knobDefault("Saturation.label", "<b> mix: [value mix]")

    # CONVOLUTIONS
    nuke.knobDefault("Denoise2.useGPUIfAvailable", "1")
    nuke.knobDefault("Blur.channels", "rgba")
    nuke.knobDefault("Blur.label", "<b> [value size] px")
    nuke.knobDefault("Dilate.channels", "rgba")
    nuke.knobDefault("Dilate.label", "<b> [value size] px")
    nuke.knobDefault("FilterErode.label", "<b> [value size] px")
    nuke.knobDefault("Erode.label", "<b> [value size] px")
    nuke.knobDefault("Median.label", "<b> [value size] px")
    nuke.knobDefault("Soften.channels", "rgba")
    nuke.knobDefault("Soften.label", "<b> [value size] px")
    nuke.knobDefault("Sharpen.channels", "rgb")
    nuke.knobDefault("Sharpen.label", "<b> [value size] px")
    nuke.knobDefault("GodRays.channels", "rgba")
    nuke.knobDefault("Bokeh.worldScaleMultiplier", "10")
    nuke.knobDefault("VectorBlur.channels", "rgba")

    # MERGE
    nuke.knobDefault("Switch.which", "1")
    nuke.knobDefault("Switch.label", "<b> [value which]")
    nuke.knobDefault("Dissolve.which", "1")
    nuke.knobDefault("Dissolve.label", "<b> [value which]")
    nuke.knobDefault("Keymix.bbox", "1")
    nuke.knobDefault("Keymix.channels", "rgba")
    nuke.knobDefault("Merge2.bbox", "3")
    nuke.knobDefault("Merge2.label", "<b> mix: [value mix]")

    # TRANSFORM
    nuke.knobDefault("Transform.shutteroffset", "centered")
    nuke.knobDefault("TransformMasked.shutteroffset", "centered")
    nuke.knobDefault("CornerPin2D.shutteroffset", "centered")
    nuke.knobDefault("Tracker4.shutteroffset", "centered")
    nuke.knobDefault("Card3D.shutteroffset", "centered")
    nuke.knobDefault("Reconcile3D.shutteroffset", "centered")
    nuke.knobDefault("Mirror.Horizontal", "1")
    nuke.knobDefault("Mirror2.flop", "1")
    nuke.knobDefault("Reformat.label", "<b> [value filter]")
    nuke.knobDefault("Reformat.pbb", "true")

    # 3D
    nuke.knobDefault("ScanlineRender.antialiasing", "3")
    nuke.knobDefault("ScanlineRender.label", "<b> samples: [value samples]")
    nuke.knobDefault("ScanlineRender.shutteroffset", "centered")

    # MISC
    nuke.knobDefault("Expression.label", "<b> [knob expr3]")
    nuke.knobDefault("DeepReformat.pbb", "1")
    nuke.knobDefault("DeepReformat.resize", "none")
    nuke.knobDefault("STMap.channels", "rgba")
    nuke.knobDefault("STMap.uv", "rgb")
    nuke.knobDefault("AdjBBox.numpixels", "100")
    nuke.knobDefault("AdjBBox.label", "<b> [value numpixels]")
    nuke.knobDefault("Constant.channels", "rgba")
    nuke.knobDefault("VectorDistort.label", "<b> REF: [value reference_frame]")

# Run it once on startup
nodeDefaultsStartup()
