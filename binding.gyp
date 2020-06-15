{
  'targets': [
    {
      'defines': [
        'NOMINMAX',
        'UNICODE',
        'WIN32_LEAN_AND_MEAN',
        '_WIN32_WINNT=0x0603'
      ],
      'msvs_settings': {
        'VCCLCompilerTool': {
          'FavorSizeOrSpeed': '2',  # Favor size over speed
          'Optimization': '1',  # Optimize for size
          'RuntimeLibrary': '2',  # Multi-threaded runtime dll
        }
      },
      'target_name': 'profiler',
      'sources': [
        'src/profiler.cc',
        'src/cpu_profiler.cc',
        'src/cpu_profile.cc',
        'src/cpu_profile_node.cc'
      ],
      'include_dirs' : [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
